<?php

require_once( dirname( dirname( __FILE__ ) ) . '/wp-load.php' );

if ( current_user_can( 'administrator' ) ) {
    $current_user = wp_get_current_user();

    echo "Bonjour " . $current_user->user_login . "!<br /><br />Le cache a été vidé et il est en cours de re-création, cette opération peut nécessiter de 15 à 20 minutes...";


	exec("/usr/bin/rm -rf /home/jazirat1/lscache/*");
        exec("> /home/jazirat1/precache.log");

	exec("/usr/bin/ps aux | grep chrome | awk \"{print \$2}\" | while read i; do kill -9 \$i; done");
	exec("/usr/bin/ps aux | grep python3 | awk \"{print \$2}\" | while read i; do kill -9 \$i; done");

	sleep(1);

	exec("/usr/bin/python3 /home/jazirat1/public_html/wp-admin/lscache.py > /dev/null 2>&1 &");

} else {
    echo "Access denied!";
}

?>
