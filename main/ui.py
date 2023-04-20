def quit():
    del runer
def load(op):
    import cmd
    app = cmd.Cmd(op)
    return app