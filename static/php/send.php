<?php 
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];
$subject = $_POST['subject'];
$rating = $_POST['rating']

$to = 'abhi12.p@gmail.com';
$message = 'FROM: '.$name.' Email: '.$email.'Message: '.$message.' With a Rating of: '.$rating;
$headers = 'From: youremail@domain.com' . "\r\n";
 
if (filter_var($email, FILTER_VALIDATE_EMAIL)) { // this line checks that we have a valid email address
mail($to, $subject, $message, $headers); //This method sends the mail.
echo "Your email was sent!"; // success message
}else{
echo "Invalid Email, please provide an correct email.";
}

?>