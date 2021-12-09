from pyparsing import *
from common import stepNode, stepMap

# ParserElement.setDefaultWhitespaceChars(' \n\t')

fatherNode = stepNode("no name")
condition = ""

def stepCheck(s: str, loc: int, tokens: ParseResults):
    stepName = tokens.get("fatherName")
    fatherNode = stepMap.get(stepName, None)
    if  fatherNode is None:
        fatherNode = stepNode(stepName)
        stepMap.update({stepName: fatherNode})
    pass

def stepBranch(s: str, loc: int, tokens: ParseResults):
    if len(fatherNode.steps) == 0 or fatherNode.steps[-1] != "BRANCH":
        fatherNode.steps.append("BRANCH")
    condition = tokens.get("condition")
    stepName = tokens.get("sonName")
    fatherNode.addNode(stepName, condition)
    pass

def stepWait(s: str, loc: int, tokens: ParseResults):
    pass
    
stepName = Combine("Proc:" + Word(alphas))
# func = Word(srange("[A-Z]")).setResultsName("funcName")
branchInput = Word(alphas)
branch_detail = ("BRANCH" + branchInput.setResultsName("condition") + stepName.setResultsName("sonName")).setParseAction(stepBranch)
wait_detail = ("WAIT" + Word(nums) + Word(nums)).setParseAction(stepWait)
detail = branch_detail
begin = ("step" + stepName.setResultsName("fatherName")).setParseAction(stepCheck)
end = Literal("end") + Literal("step")
step = begin + OneOrMore(detail) + end
instruction = OneOrMore(step)


def parse(shell: str):
    return instruction.parse_string(shell)