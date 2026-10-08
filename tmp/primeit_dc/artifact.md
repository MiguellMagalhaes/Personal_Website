# PrimeIT Professional Skills Document Template Contract

## Reference

- Source: `/Users/miguelmagalhaes/Downloads/Template DC.docx`
- SHA-256: `859e2ceebc11a97d00228b24a506b57f4bde85d12c9d3c563b63fbe59e60942c`
- Render: `/Users/miguelmagalhaes/Documents/GitHub/Personal_Website/tmp/primeit_dc/template-render`
- Page count: 4
- Section count: 1
- Source remains read-only and must not be overwritten.

## Page system

- A4 portrait, 8.27 x 11.69 inches.
- Margins: left 0.89 in, right 0.89 in, top 1.57 in, bottom 1.18 in.
- One continuous section with a distinct first-page header and footer.
- Full-page anchored brand artwork is retained in `header1.xml` and `header2.xml`.
- Footer artwork, confidentiality text and PAGE fields are retained. Candidate name in the footer is editable.
- Manual page breaks separate summary, technical skills, professional experience, and education/languages.

## Typography and components

- Retain all source styles, direct formatting, green/grey branding, table rules, spacing, and page furniture.
- Cover uses large green candidate name, large grey target role, and a smaller bracketed experience line.
- Section labels are uppercase, dark grey/black and source-formatted.
- Summary is concise prose in the source Title style.
- Technical skills use a three-column table: technology, level 1 to 5, and type.
- Professional experience uses a repeated four-row, one-column table pattern: role/date, context, activities, technologies.
- Education uses a three-column table: year, training, institution.
- Languages use a four-column table: language, understanding, speaking, writing.

## Slot map

- `word/document.xml` body paragraphs 4 to 6: candidate name, target role, experience label.
- Body paragraphs 11, 13, 15, 17 and 19: experience summary content; unused paragraphs may be cleared but their structure is retained.
- Table 0: replace the sample technology rows with confirmed professional or academic skills only.
- Tables 1 to 3: replace sample professional experience entries. A fourth entry may be created by cloning the source experience-table pattern because the candidate has four supported roles.
- Table 4: replace sample education rows and add supported certification rows using the same table pattern.
- Table 5: replace language levels with Portuguese C2 and English B2.
- `word/footer2.xml` and `word/footer3.xml`: replace the sample candidate name with Miguel Magalhães while preserving PAGE fields and artwork.
- Remove all names and claims belonging to the sample candidate, including Davide Alves and Luciano Vieira.

## Content constraints

- Write the dossier in English to match the supplied template and vacancy.
- Target profile: IT Support Technician, with emphasis on L1 support, incident handling, Windows, Active Directory, Microsoft 365, networking and SQL.
- Do not claim Murex, PowerShell, VMWare, VEEAM, NAKIVO, Palo Alto, Hyper-V, Crystal Reports or other unsupported technologies.
- Keep skill levels conservative and distinguish Professional from Academic experience.
- Keep the candidate's preference to omit Supabase from the freelance experience.

## Package preservation

- Preserve-only: theme, styles, numbering, settings, font table, web settings, custom XML, all media, all image relationships, footnotes, endnotes, headers, footer artwork and PAGE fields.
- Editable: `word/document.xml`, footer candidate-name text, and document core metadata.
- Baseline package inventory and hashes were captured in the task log before editing.

## Fidelity gates

- Reference geometry, brand artwork, headers, footer shapes, confidentiality wording, page-number fields, table styling and typography must remain source-derived.
- Render every final page and inspect at 100 percent.
- Confirm no sample-candidate names or unsupported technologies remain.
- Confirm page furniture, page numbers, tables, bullets and text remain unclipped and aligned.
- Confirm the retained source still matches the recorded SHA-256 after completion.
