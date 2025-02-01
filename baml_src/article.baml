class Article {
    tile string
    date string
    author string
    summary string
    content string
}


function ExtractArticle(article: string) -> Article {
    client Llama
    prompt #"
        Extract from this content:
        {{ article }}

        {{ ctx.output_format }}
    "#
}