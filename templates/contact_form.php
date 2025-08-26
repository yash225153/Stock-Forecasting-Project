<?php
// Database configuration
$host = "localhost";
$db_name = "contact_form";
$username = "root"; // Change to your database username
$password = ""; // Change to your database password

// Connect to the database
$conn = new mysqli($host, $username, $password, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve and sanitize form data
    $name = htmlspecialchars($_POST["name"]);
    $email = htmlspecialchars($_POST["email"]);
    $phone = htmlspecialchars($_POST["phone"]);
    $project = htmlspecialchars($_POST["project"]);
    $subject = htmlspecialchars($_POST["subject"]);
    $message = htmlspecialchars($_POST["message"]);

    // Validate required fields
    if (empty($name) || empty($email) || empty($subject) || empty($message)) {
        echo "Please fill in all required fields.";
        exit;
    }

    // Prepare SQL query
    $stmt = $conn->prepare("INSERT INTO messages (name, email, phone, project, subject, message) VALUES (?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("ssssss", $name, $email, $phone, $project, $subject, $message);

    // Execute query
    if ($stmt->execute()) {
        echo "Thank you! Your message has been received.";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close statement
    $stmt->close();
}

// Close database connection
$conn->close();
?>
