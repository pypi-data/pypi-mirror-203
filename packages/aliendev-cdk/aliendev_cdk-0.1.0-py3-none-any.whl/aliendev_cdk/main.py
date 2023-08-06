import typer
from aliendev_cdk.service import loginService, registerService

app = typer.Typer()

@app.command("register")
def register():
    registerService.register()
    
@app.command("login")
def login():
    loginService.login()

@app.command("deploy")
def deploy():
    pass

if __name__ == "__main__":
    app()