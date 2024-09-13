from textnode import TextNode

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

        if self.props == None:
            return ""

        for key, value in self.props.items():
            res.append(f' {key}="{value}"')
        
        repr = "".join(res)
        return repr

class LeafNode(HTMLNode):
     
     def __init__(self, tag, value, props=None):
          
          super().__init__(tag, value, props)
     
     def to_html(self):
          
          built_string = ""

          if not self.value:
               raise ValueError("Leaf nodes must have a value")
          
          if not self.tag:
               return self.value
          
          start_tag_string = f"<{self.tag}"
          built_string += start_tag_string

          if self.props != None:
               for key, value in self.props.items():
                    built_string += (f' {key}="{value}"')
          
          built_string += ">"
          
          built_string += self.value
          
          end_tag_string = f"</{self.tag}>"
          built_string += end_tag_string

          return built_string
     
     def __repr__(self):

        return f"LeafNode({self.tag}, {self.value}, {self.props})"
     
class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):

        super().__init__(tag, None, children, props)

    def to_html(self):

        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        
        children_html = ""

        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):

        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

def text_node_to_html_node(text_node):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

    if text_node.text_type == text_type_text:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode(tag='b', value=text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode(tag='i', value=text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode(tag='a', value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode(tag="img", value="", props={"src", text_node.url, "alt", text_node.alt})
    else:
        raise Exception("Invalid text type.")
   









        






