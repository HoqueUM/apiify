class Article {
    title string
    date string
    author string
    summary string
    content string
}

function ExtractArticle(article: string) -> Article {
    client Mistral
    prompt #"
        Extract from this content:
        {{ article }}

        {{ ctx.output_format }}
    "#
}