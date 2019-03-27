
from app import create_app, db, cli
from app.models import User, Post, Notification, Message, Task

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    #新模型也可以添加到shell上下文中，以便在shell会话中访问它时无需导入
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,\
            'Notification': Notification, 'Task': Task}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5010)

