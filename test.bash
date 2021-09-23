#!/bin/bash
fname=../test_export/Draft/"Agile_Takeaways.txt"
echo $fname
parse $fname rmcomments.ohm rmcomments.glue
