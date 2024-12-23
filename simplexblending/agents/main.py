from hyperon import *
from methods import *
from hyperon.ext import register_atoms

@register_atoms(pass_metta=True)
def grounded_atoms(metta):
    
    llmAtom = OperationAtom('llm', lambda *args: call_openai(metta, *args),  [AtomType.ATOM, AtomType.ATOM ], unwrap=False)

    return {
        r"llm": llmAtom
    }