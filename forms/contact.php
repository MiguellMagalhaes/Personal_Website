<?php
// Verifica se o formulário foi enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Obtém e sanitiza os dados do formulário
    $name    = strip_tags(trim($_POST["name"]));
    $name    = str_replace(array("\r","\n"), array(" "," "), $name);
    $email   = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $subject = trim($_POST["subject"]);
    $message = trim($_POST["message"]);

    // Verifica se os campos obrigatórios estão preenchidos e se o email é válido
    if ( empty($name) || empty($subject) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL) ) {
        // Resposta de erro (400 - Bad Request)
        http_response_code(400);
        echo "Please complete the form and try again.";
        exit;
    }

    // Define o destinatário
    $recipient = "trabalhosdomike@gmail.com";

    // Define o assunto do email
    $email_subject = "New Contact Form Submission from $name: $subject";

    // Define o conteúdo do email
    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n\n";
    $email_content .= "Message:\n$message\n";

    // Define os cabeçalhos do email
    $email_headers = "From: $name <$email>";

    // Tenta enviar o email
    if (mail($recipient, $email_subject, $email_content, $email_headers)) {
        // Email enviado com sucesso (200 OK)
        http_response_code(200);
        echo "Thank you! Your message has been sent.";
    } else {
        // Se houver problema no envio (500 Internal Server Error)
        http_response_code(500);
        echo "Oops! Something went wrong and we couldn't send your message.";
    }

} else {
    // Se o formulário não foi enviado via POST, retorna 403 Forbidden
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
?>