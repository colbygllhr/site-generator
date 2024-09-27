def markdown_to_blocks(markdown):
    lines = markdown.split('\n\n') # Double newline to specify paragraph

    stripped = [line.strip() for line in lines if line.strip()]

    return stripped

    

        
    
        

        



    
