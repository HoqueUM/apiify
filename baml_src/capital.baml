class CountryCapital {
    country string
    capital string
}

function ExtractCountryCapital(text: string) -> CountryCapital {
    client Deepseek
    prompt #"
        Extract the country and its capital from the given text:
        {{ text }}

        {{ ctx.output_format }}
    "#
}