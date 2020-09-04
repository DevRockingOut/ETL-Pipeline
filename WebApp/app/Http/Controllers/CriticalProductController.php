<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\CriticalProduct;

class CriticalProductController extends Controller
{
    public function index()
    {
        $products = CriticalProduct::all();

        return view('critical_products', compact('products'));
    }
}
