class PageData {
    @@dynamic
}

class Metadata {
    part string @description(#"
        The content part that was extracted.
        "#)
    tag string @description(#"
        The HTML tag that contains the content.
        "#)
    content string @description(#"
        The content of the HTML tag. This should not be HTML.
        This should be the content that is visible to the user.
        It should align with the part.
        "#)
    attributes Atrribute[]
}

class Atrribute {
    attribute string @description(#"
        The attributes of the HTML tag.
        This could be class, id, href, etc.
    "#)
    value string @description(#"
        The value of the attribute.
    "#)
}

function ExtractPageData(parts: string[], HTML: string) -> PageData {
    client Mistral
    prompt #"
       Task: Extract exact HTML snippets containing specific content.

        For each of the following content parts:
        {% for part in parts %}
        - {{part}}
        {% endfor %}

        Instructions:
        1. Extract the full HTML of that element, including its tags and all attributes.
        2. Preserve the exact formatting, spacing, and attribute order as in the original HTML.
        3. Choose the innermost element that fully encapsulates the required content.        
        4. Prioritize elements with identifying attributes (e.g., class, id) that are directly related to the content.
        5. If a part is not found, attempt to interpret what the most likely content would be. Otherwise, leave it blank.
        6. If multiple elements match, choose the most logical option.
        7. Pretend that you are extracting this data for a database using some 
              kind of web scraping tool. It is necessary to to keep it clean
              and accurate. Do not overly generalize the content.

        HTML Source:
        {{ HTML }}

        {{ ctx.output_format }}

    "#
}

function FilterPageData(parts: string[], HTML: string) -> Metadata[] {
    client Mistral
    prompt #"
       Task: Extract data from this HTML.

        For each of the following content parts:
        {% for part in parts %}
        - {{part}}
        {% endfor %}

        Instructions:
        1. Extract as many values as you can.
        2. Be as specific as possible. Do not leave the content portion as HTML.
        3. If a part is not found, leave it blank.
        4. Pretend that you are extracting this data for a database using some 
              kind of web scraping tool. It is necessary to to keep it clean
              and accurate. Do not overly generalize the content.

        HTML Source:
        {{ HTML }}
    
        {{ ctx.output_format }}

    "#
}