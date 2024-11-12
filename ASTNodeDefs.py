# Base class for all AST nodes
class ASTNode:
    def to_string(self):
        """Method to provide compact string representation without newlines."""
        return repr(self)

# Class for variable assignment: x = expression
class Assignment(ASTNode):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def __repr__(self):
        return f"Assignment({self.identifier}, {self.expression})"

    def to_string(self):
        expr_str = self.expression.to_string() if isinstance(self.expression, ASTNode) else repr(self.expression)
        return f"Assignment({self.identifier}, {expr_str})"

# Class for variable declarations: int x = expression or float x = expression
class Declaration(ASTNode):
    def __init__(self, var_type, identifier, expression=None):
        self.var_type = var_type  # 'int' or 'float'
        self.identifier = identifier
        self.expression = expression

    def __repr__(self):
        expr_repr = repr(self.expression) if self.expression is not None else "None"
        return f"Declaration({self.var_type}, {self.identifier}, {expr_repr})"

    def to_string(self):
        expr_str = self.expression.to_string() if isinstance(self.expression, ASTNode) else repr(self.expression)
        return f"Declaration({self.var_type}, {self.identifier}, {expr_str})"

# Class for binary operations: term1 + term2
class BinaryOperation(ASTNode):
    def __init__(self, left, operator, right, value_type=None):
        self.left = left
        self.operator = operator
        self.right = right
        self.value_type = value_type  # Type of the result of the operation (e.g., int or float)

    def __repr__(self):
        return f"BinaryOperation({self.left}, {self.operator}, {self.right}, type={self.value_type})"

    def to_string(self):
        left_str = self.left.to_string() if isinstance(self.left, ASTNode) else repr(self.left)
        right_str = self.right.to_string() if isinstance(self.right, ASTNode) else repr(self.right)
        return f"BinaryOperation({left_str}, {self.operator}, {right_str}, type={self.value_type})"

# Class for boolean expressions: x != 10
class BooleanExpression(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"BooleanExpression({self.left}, {self.operator}, {self.right})"

    def to_string(self):
        left_str = self.left.to_string() if isinstance(self.left, ASTNode) else repr(self.left)
        right_str = self.right.to_string() if isinstance(self.right, ASTNode) else repr(self.right)
        return f"BooleanExpression({left_str}, {self.operator}, {right_str})"

# Class for function calls: foobar(arg1, arg2)
class FunctionCall(ASTNode):
    def __init__(self, function_name, arguments):
        self.function_name = function_name
        self.arguments = arguments

    def __repr__(self):
        args_repr = ", ".join(repr(arg) for arg in self.arguments)
        return f"FunctionCall({self.function_name}, [{args_repr}])"

    def to_string(self):
        args_str = ", ".join(arg.to_string() if isinstance(arg, ASTNode) else repr(arg) for arg in self.arguments)
        return f"FunctionCall({self.function_name}, [{args_str}])"

# Class for if statements
class IfStatement(ASTNode):
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def __repr__(self):
        else_repr = repr(self.else_block) if self.else_block is not None else "None"
        return f"IfStatement({self.condition}, {self.then_block}, {else_repr})"

    def to_string(self):
        condition_str = self.condition.to_string() if isinstance(self.condition, ASTNode) else repr(self.condition)
        then_str = self.then_block.to_string() if isinstance(self.then_block, ASTNode) else repr(self.then_block)
        else_str = self.else_block.to_string() if self.else_block is not None else "None"
        return f"IfStatement({condition_str}, {then_str}, {else_str})"

# Class for while statements
class WhileStatement(ASTNode):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

    def __repr__(self):
        return f"WhileStatement({self.condition}, {self.block})"

    def to_string(self):
        condition_str = self.condition.to_string() if isinstance(self.condition, ASTNode) else repr(self.condition)
        block_str = self.block.to_string() if isinstance(self.block, ASTNode) else repr(self.block)
        return f"WhileStatement({condition_str}, {block_str})"

# Class for blocks
class Block(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        statement_reprs = "\n  ".join(repr(statement) for statement in self.statements)
        return f"Block(\n  {statement_reprs}\n)"

    def to_string(self):
        statement_strs = ", ".join(stmt.to_string() if isinstance(stmt, ASTNode) else repr(stmt) for stmt in self.statements)
        return f"Block([{statement_strs}])"

# Class for factors (literals or variables) in expressions
class Factor(ASTNode):
    def __init__(self, value, value_type):
        self.value = value
        self.value_type = value_type  # 'int', 'float', or other types as needed

    def __repr__(self):
        return f"Factor(value={self.value}, type={self.value_type})"

    def to_string(self):
        return f"Factor(value={self.value}, type={self.value_type})"
