<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  
  // Coletar os dados do formulário
  $name = strip_tags($_POST['name']);
  $email = strip_tags($_POST['email']);
  $subject = strip_tags($_POST['subject']);
  $message = strip_tags($_POST['message']);

  // Configura destinatário
  $to = 'trabalhosdomike@gmail.com'; 

  // Assunto (pode usar $subject ou forçar algo fixo)
  $mailSubject = $subject;

  // Cabeçalhos
  $headers = "From: $email\r\n";
  $headers .= "Reply-To: $email\r\n";
  $headers .= "Content-Type: text/html; charset=UTF-8\r\n";

  // Corpo do email
  $mailBody = "<h2>Nova mensagem do site</h2>"
    . "<p><strong>Nome:</strong> $name</p>"
    . "<p><strong>Email:</strong> $email</p>"
    . "<p><strong>Assunto:</strong> $subject</p>"
    . "<p><strong>Mensagem:</strong><br>" . nl2br($message) . "</p>";

  // Envia
  if (mail($to, $mailSubject, $mailBody, $headers)) {
    echo 'OK';  // O validate.js espera ver "OK" para indicar sucesso.
  } else {
    echo 'ERROR: Could not send mail!';
  }
} else {
  echo 'ERROR: Invalid request';
}
?>