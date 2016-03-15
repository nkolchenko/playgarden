#!/usr/bin/perl

use strict;
use warnings;

my $file1="tail_sip.log";
print "$file1\n";

open(HANDLE, "$file1") || die "Unable to open $file1";

my $lines_count = 0;
my $block = "";

while(my $line = <HANDLE>){
    chomp($line);
    $lines_count++;
    unless ($line =~ /^\s*$/)
     {
#       print "$line\n";
        my $in_message=1;
#        $lines_count++;
        if ($in_message==1 && $line =~ /message\ to/ )
        {
                print "$line\n";
                print "\n";
        }
     }
}
print "TOTAL Lines Processed: $lines_count\n";



close(HANDLE);
####    
sub trim
{
    my $string = shift;

    $string =~ s/^\s+//;
    $string =~ s/\s+$//;

    return $string;
}

