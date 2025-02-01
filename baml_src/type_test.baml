class PageData {
    @@dynamic
}

function ExtractPageData(input: string) -> PageData {
    client Llama
    prompt #"
        Extract the html that contains these from this content.
        Give me the html only. Not the text:
        {{ input }}

        {{ ctx.output_format }}
    "#
}