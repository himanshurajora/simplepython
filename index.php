<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<?php 
function commentsare($tableis){
    $con = mysqli_connect('localhost', 'root', '', 'comments');
    $q = "SELECT comment FROM ".$tableis;
    $result = mysqli_query($con, $q);
    echo mysqli_num_rows($result);
    
    while($row = mysqli_fetch_assoc($result)){
       echo $row['comment']."<br>";
    }
}


?>
    <?php
    $username = "himanshu";
    $con = mysqli_connect('localhost', 'root', '', 'example');
    $con2 = mysqli_connect('localhost', 'root', '', 'comments');
    if (isset($_POST['submit'])) {
        $data = $_POST['data'];
        $q = "INSERT INTO posts(data) VALUE('" . $data . "')";

        if (mysqli_query($con, $q)) {
            $q2 = "SELECT id FROM posts WHERE data =  '" . $data . "'";
            $result = mysqli_query($con, $q2);
            if (mysqli_num_rows($result) > 0) {
                while ($row = mysqli_fetch_assoc($result)) {
                    $id = $row['id'];
                }
            }
            echo "data saved successfully";
        }

        $q3 = "CREATE TABLE c" . $username . $id . "(
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    comment TEXT NOT NULL
)";
        $tablename = "c" . $username . $id;
        $q4 = "UPDATE posts SET comments = '" . $tablename . "' WHERE id = " . $id;
        if (mysqli_query($con, $q4)) {
            echo 'comments Added';
        } else {
            echo mysqli_error($con);
        }
        if (mysqli_query($con2, $q3)) {
            echo 'tablecreated Successfully';
        } else {
            echo mysqli_error($con2);
        }
    }


    ?>
    <div class="cpost">
        <div class="cpost-input">
            <h4>Create A post</h4>
            <form method="post">
                <label for="data">Data</label>
                <input type="text" name="data">
                <input type="submit" name="submit">
            </form>
        </div>
    </div>
    <HR>
    </HR>
    <div class="vpost">
        <h4>Posts:</h4>
        <style>
            .posts {
                border: 1px solid black;
                height: 500px;
                width: 300px;
            }

            .data {
                border: 1px solid black;
                height: 25%;
                width: auto;
            }

            .comments {
                border: 1px solid black;
                height: 75%;
                width: auto;
                overflow: auto;
            }
        </style>
        <div>
            <?php
            $commenttable = "";
            if (isset($_POST['comment'])) {
                $commentdata = $_POST['commentdata'];
                $commenttable = $_POST['tablename'];
                addComment($con2, $commentdata, $commenttable);
            }
            $q5 = "SELECT data, comments FROM posts";

            $postresult = mysqli_query($con, $q5);
            if (mysqli_num_rows($postresult) > 0) {
                while ($row = mysqli_fetch_assoc($postresult)) {
                    $data = $row['data'];
                    $commenttable = $row['comments'];
                    $q6 = "SELECT comment FROM " . $commenttable;
                    echo  '<div class="posts">
                    <div class="data"><h1>' . $data . '</h1></div>
                    <form method=post>
                        <input type="text" name="commentdata">
                        <input type="hidden" name="tablename" value="' . $commenttable . '">
                        <input type="submit" name="comment">
                    </form><div class="comments">';
                    
                    commentsare($commenttable);
                    // echo $q6;
                    // showComments($con2, $q6);

                    echo '
                    </div>
                    </div>
                    </div>';
                }
            }

            function addComment($con2, $commentdata, $commenttable)
            {
                $q7 = "INSERT INTO " . $commenttable . "(comment) 
                        VALUE('" . $commentdata . "')";
                if (!mysqli_query($con2, $q7)) {
                    echo mysqli_error($con2);
                }
            }
            function showComments($con2, $q6)
            {
                    while ($row2 = mysqli_fetch_assoc(mysqli_query($con2, $q6))) {
                        echo $row2['comment'];
                        // $comment = $row['comment'];
                        // echo '<p>' . $comment . '</p>';
                    }
            }
            ?>
        </div>

</body>

</html>


<!-- <div class="posts">
        <div class="data"><h1>dataHere</h1></div>
        <form method=post>
            <input type="text" name="commentdata">
            <input type="hidden" name="tablename" value="example">
            <input type="submit" name="comment">
        </form>
        <div class="comments">
        <p>comments here</p>
        </div>
    </div>
    </div> -->