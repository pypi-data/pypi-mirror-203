from abc import ABC, abstractmethod
import os
from pathlib import Path

from .retry import RetryStrategyFactory, CompleteRetry, IncrementalRetry
from .state import RFState
from ..target import LocalTarget
from ...strategies import RunStrategy

from robotmk.logger import RobotmkLogger
from robotmk.config import Config

import robot
import mergedeep


from datetime import datetime

local_tz = datetime.utcnow().astimezone().tzinfo

# This is the "heavy" part of the code. It contains the logic to run RF.
# Here I place all the Robotmk v1 shit.


class RobotFrameworkTarget(LocalTarget):
    def __init__(
        self,
        suiteuname: str,
        config: dict,
        logger: RobotmkLogger,
    ):
        super().__init__(suiteuname, config, logger)

        self.retry_strategy = RetryStrategyFactory(self).create()

        self.shortuuid = self.uuid[:8]
        # this timestamp is used to keep all result files in order; it is used
        # for all target executions
        self._timestamp = self.get_now_as_epoch()
        self._state = RFState(self)
        # params for RF: global ones & re-execution
        # self.robot_params = {"console": "NONE", "report": "NONE"}
        self.robot_params = {"report": "NONE"}

    def __str__(self) -> str:
        return "robotframework"

    @property
    def command(self):
        """The command will be used by the Run strategy (self.target.command).

        In RF target, the complete commandline must be built to execute the RF suite.
        (See https://robot-framework.readthedocs.io/en/latest/autodoc/robot.html#robot.run.run_cli)
        TODO: Logging"""
        self.robot_params.update(
            {
                "log": self.log_html,
                "output": self.output_xml,
            }
        )

        suite_params = mergedeep.merge(
            {}, self.config.get("suitecfg.params").asdict(), self.robot_params
        )
        arglist = ["robot"]
        for k, v in suite_params.items():
            arg = f"--{k}"
            # create something we can iterate over
            if isinstance(v, str):
                # key:value    => convert to 1 el list
                vlist = [v]
            elif isinstance(v, dict):
                if k == "variable":
                    # key:var-dict => convert to list of varkey:varvalue
                    vlist = list(map(lambda x: f"{x[0]}:{x[1]}", v.items()))
                else:
                    self._suite.logger.warn(
                        f"The Robot Framework parameter {k} is a dict but cannot be converted to cmdline arguments (values: {str(v)})"
                    )
            elif isinstance(v, list):
                if k == "argumentfile" or k == "variablefile":
                    # make the file args absolute file paths
                    v = [str(self._suite.pathdir.joinpath(n)) for n in v]
                # key:list     => no conversion
                vlist = v

            for value in vlist:
                # values which are boolean(-like) are single parameters without option
                if type(value) is bool or value in ["yes", "no", "True", "False"]:
                    arglist.extend([arg])
                else:
                    arglist.extend([arg, value])
        # the path of the robot suite is the very last argument
        arglist.append(str(self.path))
        return arglist

    def run(self):
        # Do not run if the suite dir contains a DISABLED file
        if self.is_disabled_by_flagfile:
            # TODO: Log skipped
            # reason = self.get_disabled_reason()
            return
        else:
            # Tell Robot Framework to write its "output" files into the log dir.
            # The "outputdir" is where RMK produces files later for the agent.
            self.robot_params.update(
                {"outputdir": str(Path(self.logdir).joinpath("robotframework"))}
            )
            self._state.timer_start()
            self.rc = self.retry_strategy.run()
            self._state.timer_stop()
            self._state.write()
            pass

    def get_now_as_dt(self):
        return datetime.now(local_tz)

    def get_now_as_epoch(self):
        return int(self.get_now_as_dt().timestamp())

    @property
    def outdir(self):
        return self.config.get("common.outdir")

    @property
    def timestamp(self):
        """Returns the timestamp the suite execution was started. This is
        used for all executions of the suite, including retries in order
        to group the result files."""
        return self._timestamp

    def get_disabled_reason(self) -> str:
        """Report back the reason why the suite was disabled."""
        if self.is_disabled_by_flagfile:
            try:
                with open(self.path.joinpath("DISABLED"), "r") as f:
                    reason = f.read()
                    if len(reason) > 0:
                        return "Reason: " + reason
                    else:
                        return ""
            except:
                return ""

    @property
    def output_filename(self):
        """Returns the output filename string, including the retry number.

        Example:
            rf_suite1_978741fb_1680335851
            rf_suite1_978741fb_1680335851-1"""
        if self.attempt is None:
            suite_filename = "rf_%s_%s_%s" % (
                self.suiteuname,
                self.timestamp,
                self.shortuuid,
            )
        else:
            suite_filename = "rf_%s_%s_%s-%d" % (
                self.suiteuname,
                self.timestamp,
                self.shortuuid,
                int(self.attempt),
            )
        return suite_filename

    @property
    def statefile_fullpath(self):
        return str(Path(self.outdir).joinpath(self.suiteuname + ".json"))

    # XML ---
    @property
    def output_xml(self):
        return self.output_filename + ".xml"

    @property
    def output_xml_fullpath(self):
        return str(Path(self.robot_params["outputdir"]).joinpath(self.output_xml))

    # HTML ---
    @property
    def log_html(self):
        return self.output_filename + ".html"

    @property
    def log_html_fullpath(self):
        return str(Path(self.robot_params["outputdir"]).joinpath(self.log_html))

    # Suite timestamp for filenames
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, t):
        self._timestamp = t
