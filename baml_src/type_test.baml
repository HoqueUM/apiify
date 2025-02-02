class PageData {
    @@dynamic
}

function ExtractPageData(parts: string[], HTML: string) -> PageData {
    client Mistral
    prompt #"
        I would like help extract parts of this HTML. Not the content, but the actual HTML of the page.
        Give me the exact HTML, as it is of these things:

        {% for part in parts %}
            {{part}} 
        {% endfor %}
        
        From this HTML:
        {{ HTML }}

        {{ ctx.output_format }}

    "#
}