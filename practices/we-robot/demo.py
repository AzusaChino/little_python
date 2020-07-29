import werobot

robot = werobot.WeRoBot(token="TheToken")


@robot.handler
def hello(message):
    return "Hello " + message


robot.config['HOST'] = "127.0.0.1"
robot.config['PORT'] = "9090"

robot.run()
