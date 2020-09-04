<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Optioma Analytics - ETL Pipeline</title>

        <style>
            #container{
                margin:0 auto;
                width:50%;
                text-align:center;
            }

            #container table {
                width:100%;
            }

            #container table th {
                font-size:1.2em;
            }

            #container table td {
                padding:10px;
            }
        </style>
    </head>
    <body>
        <div id="container">
            <h1>Critical Products</h1>
            <table class="table table-striped">
                <thead>
                <tr>
                    <th>Name</th>
                    <th>Total</th>
                </tr>
                </thead>
                <tbody>
                
                @foreach($products as $product)
                <tr>
                    <td>{{ $product->name }}</td>
                    <td>{{ $product->total_available }}</td>
                </tr>
                @endforeach
                
                </tbody>
            </table>
        </div>
    </body>
</html>