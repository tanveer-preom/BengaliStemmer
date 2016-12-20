<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the controller to call when that URI is requested.
|
*/

Route::get('/', function () {
	$contents = "";
	$text = "";
	$filepath =" ";
    return view('welcome',compact('filepath'))->with('contents',$contents)->with('text',$text);
});

Route::get('/generate', function () {
	$contents = "";
	$text = '';
	$filepath = " ";
    return view('welcome',compact('filepath'))->with('contents',$contents)->with('text',$text);
});

Route::post('/generate', function () {
	$stammerScriptDirectory = public_path().'/BanglaStemmer/Stemmer/Stemming.py';
	if(Input::hasFile('file'))
	{
		$file = Input::file('file');
		$text = file_get_contents($file->getRealPath());
		$rootInputDirectory =  public_path() . '/Data/Input';
		$rootOutputDirectory = public_path() . '/Data/Output';
		$hashKey = substr($text, -6).rand().''.microtime(true);
		$fileName = md5($hashKey);
		$inputFileDirectory = $rootInputDirectory.'/'.$fileName.'.txt';
		$outputFileDirectory = $rootOutputDirectory.'/'.$fileName.'.txt';
		$rootLD5FileDirectory = public_path().'/RootsLD5.txt';
		if(File::put($inputFileDirectory,$text))
		{
			$cmd = 'python3 '.$stammerScriptDirectory.' '.$inputFileDirectory.' '.$outputFileDirectory.' '.$rootLD5FileDirectory;
			shell_exec($cmd);
			$contents = File::get($outputFileDirectory);
			 $filepath = '/Data/Output/'.$fileName.'.txt'; 
			return view('welcome',compact('filepath'))->with('contents',$contents)->with('text',$text);

		}

	}
	else if(Input::has('text'))
	{
		$text = Input::get('text');
		$rootInputDirectory =  public_path() . '/Data/Input';
		$rootOutputDirectory = public_path() . '/Data/Output';
		$hashKey = substr($text, -6).rand().''.microtime(true);
		$fileName = md5($hashKey);
		$inputFileDirectory = $rootInputDirectory.'/'.$fileName.'.txt';
		$outputFileDirectory = $rootOutputDirectory.'/'.$fileName.'.txt';
		$rootLD5FileDirectory = public_path().'/RootsLD5.txt';
		if(File::put($inputFileDirectory,$text))
		{
			$cmd = 'python3 '.$stammerScriptDirectory.' '.$inputFileDirectory.' '.$outputFileDirectory.' '.$rootLD5FileDirectory;
			shell_exec($cmd);
			$contents = File::get($outputFileDirectory);
			$filepath = '/Data/Output/'.$fileName.'.txt'; 
			return view('welcome',compact('filepath'))->with('contents',$contents)->with('text',$text);

		}


	}

    //return view('welcome');
});