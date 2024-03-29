<?php
include_once("config.php");

if(isset($_GET['username'])) {
    $username = $_GET['username'];

    $comm = $mysqli->prepare("DELETE FROM users WHERE username = ?");
    $comm->bind_param("s", $username);
    $comm->execute();

    if ($comm->affected_rows > 0) {
        echo "Usuari borrat correctament!";
    } else {
        echo "Error al borrar l'usuari.";
    }

    $comm->close();
} else {
    echo "No s'ha donat un usuari per borrar.";
}

$mysqli->close();
header("Location:index.php");
?>
