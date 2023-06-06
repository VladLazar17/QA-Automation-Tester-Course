from Browser import Browser


def before_all(context):
    context.Browser = Browser()


def after_all(context):
    context.Browser.close()
