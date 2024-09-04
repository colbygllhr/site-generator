class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    
    def to_html(self):
        raise (NotImplementedError) 
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def props_to_html(self):
        res = [] 

        if self.props == {}:
            return ""

        for key, value in self.props.items():
            res.append(f' {key}="{value}"')
        
        repr = "".join(res)
        return repr

        






