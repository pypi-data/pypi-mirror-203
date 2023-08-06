import ast,os

class NonDeterministicFunctionChecker:
    name = 'flake8_checker'
    version = '1.0.0'

    def __init__(self, tree, filename,config=None):
        self.tree = tree

    def run(self):
        visitor = NonDeterministicFunctionVisitor()
        visitor.visit(self.tree)
        for lineno, column, msg in visitor.messages:
            yield (lineno, column, msg, NonDeterministicFunctionChecker)


class NonDeterministicFunctionVisitor(ast.NodeVisitor):
    NON_DETERMINISTIC_FUNCTIONS = os.environ.get('NON_DETERMINISTIC_FUNCTIONS', '')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.messages = []
 
    def visit_Call(self, node):
        function_name = self.get_function_name(node)
        if function_name in self.NON_DETERMINISTIC_FUNCTIONS:
            msg = 'ND001 Non-deterministic function "{}" used'.format(function_name)
            self.messages.append((node.lineno, node.col_offset, msg))

    def get_function_name(self, node):
        if isinstance(node.func, ast.Name):
            return node.func.id
        elif isinstance(node.func, ast.Attribute):
            return node.func.attr
        return None
