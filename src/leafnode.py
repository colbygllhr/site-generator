from htmlnode import HTMLNode

class LeafNode(HTMLNode):

     def __init__(self, value, tag=None, props=None):
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
