from dknovautils.dkat import AT


class DkIpyUtils(object):

    # class attribute

    @staticmethod
    def magic_fc(cmd: str):
        assert isinstance(cmd, str) and len(cmd) > 0, 'err3581'
        AT.unimplemented()

    @staticmethod
    def magic_fr(cmd) -> any:
        AT.unimplemented()
        return None
