Class Item():
def __init__(self,name,description,weight,text=None,damage=None):
    self.name=name
    self.description=description
    self.weight=weight
    self.text=text if text is not None
    self.damage=damage if damage is not None
def __str__(self):
    return f"{self.name} : {self.description} ({self.weight}) kg)\n"
