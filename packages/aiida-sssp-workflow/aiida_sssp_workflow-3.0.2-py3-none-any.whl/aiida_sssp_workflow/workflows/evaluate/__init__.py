from abc import abstractmethod

from aiida import orm

from aiida_sssp_workflow.workflows import SelfCleanWorkChain


class _BaseEvaluateWorkChain(SelfCleanWorkChain):
    """WorkChain to calculate cohisive energy of input structure"""

    @classmethod
    def define(cls, spec):
        """Define the process specification."""
        # yapf: disable
        super().define(spec)
        spec.output('ecutwfc', valid_type=orm.Int, required=True)
        spec.output('ecutrho', valid_type=orm.Int, required=True)

        spec.exit_code(210, 'ERROR_SUB_PROCESS_FAILED_SCF',
                    message='PwBaseWorkChain of pressure scf evaluation failed.')
        # yapf: enable

    @abstractmethod
    def finalize(self):
        """Must in here write ecutwfc and ecutrho to output ports
        They are needed by the convergence workflow to read the cutoff pair
        of evalueation.
        """
