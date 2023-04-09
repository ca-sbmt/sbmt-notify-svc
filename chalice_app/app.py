from chalice import Chalice
from app.main import app
from mangum import Mangum

chalice_app = Chalice(app_name='sbmt-notify-svc')
handler = Mangum(app)

@app.lambda_function()
def main(event, context):
    return handler(event, context)