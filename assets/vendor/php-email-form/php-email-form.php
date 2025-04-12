<?php
// /assets/vendor/php-email-form/php-email-form.php

// Inclui as classes do PHPMailer (ajusta o caminho se necessário)
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';

class PHP_Email_Form {
  public $ajax = false;
  public $to;
  public $from_name;
  public $from_email;
  public $subject;
  public $smtp = array(); // Opcional, se quiseres usar SMTP
  private $messages = array();

  // Define que mensagem adicionar ao corpo do email
  public function add_message($message, $label = '', $line_breaks = 0) {
    $msg = "";
    if ($label !== '') {
      $msg .= "<strong>" . htmlspecialchars($label) . ":</strong> ";
    }
    $msg .= nl2br(htmlspecialchars($message));
    if ($line_breaks > 0) {
      $msg .= str_repeat("<br>", $line_breaks);
    }
    $this->messages[] = $msg;
  }

  // Junta todas as mensagens
  private function build_message() {
    return implode("<br><br>", $this->messages);
  }

  // Envia o email
  public function send() {
    $mail = new PHPMailer(true);
    try {
      // Se quiser SMTP, configura; caso contrário, usa a função mail() do PHP (por padrão o PHPMailer usará mail() se não for configurado SMTP)
      if (!empty($this->smtp)) {
        $mail->isSMTP();
        $mail->Host       = $this->smtp['host'];
        $mail->SMTPAuth   = true;
        $mail->Username   = $this->smtp['username'];
        $mail->Password   = $this->smtp['password'];
        $mail->SMTPSecure = isset($this->smtp['SMTPSecure']) ? $this->smtp['SMTPSecure'] : 'tls';
        $mail->Port       = $this->smtp['port'];
      }
      
      $mail->setFrom($this->from_email, $this->from_name);
      $mail->addAddress($this->to);
      $mail->Subject = $this->subject;
      $mail->isHTML(true);
      $mail->Body    = $this->build_message();

      $mail->send();
      return $this->ajax ? 'OK' : true;
    } catch (Exception $e) {
      return 'ERROR: ' . $mail->ErrorInfo;
    }
  }
}
?>