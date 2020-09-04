<?php

namespace App;

use Illuminate\Database\Eloquent\Model;
use Jenssegers\Mongodb\Eloquent\Model as Eloquent;

class CriticalProduct extends Eloquent
{
    protected $connection = 'mongodb';
    protected $collection = 'critical_products';
    
    // properties
    protected $fillable = [
        'name', 'total_available'
    ];
}
