class ArgumentParser:
    @staticmethod
    def parse_args(args):
        parsed = {}
        for prop in args:
            if len(prop) > 1:
                if prop[0] == '-':
                    if '='.join(prop[1:].split('=')[:-1]) != '':
                        parsed['='.join(prop[1:].split('=')[:-1])] = prop[1:].split('=')[-1]
                    else:
                        parsed[prop[1:].split('=')[-1]] = ''

        return parsed