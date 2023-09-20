import azure.functions as func
from .file1 import some_function_in_file1
from .file2 import some_function_in_file2

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Call functions from file1 and file2
    result1 = some_function_in_file1()
    result2 = some_function_in_file2()

    return func.HttpResponse(
        f"Hello, Azure Function!\nResult from file1: {result1}\nResult from file2: {result2}",
        mimetype="text/plain",
    )
