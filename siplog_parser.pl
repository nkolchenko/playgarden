#!/usr/bin/perl

use strict;
use warnings;

#### USAGE    ./siplog_parser.pl file_name

#my $file1="sip_log";
my $file1=@ARGV[0];
print "$file1\n";

open(HANDLE, "$file1") || die "Unable to open $file1";

my $in_message = 0;
my $lines_count = 0;
my $incoming = 0;
my $outgoing = 0;
my $block = "";



while(my $line = <HANDLE>){
    chomp($line);
    $lines_count++;
#    print "$line\n";
###
### FOR NON EMPTY LINES
###
    if ($line =~ /^\S/){
        $in_message++;           
        if ($in_message !=0){ 
####
#### INCOMING messagess processing
####
		if ($line =~ /proxy\[.*\]: RECEIVED message from/ ){
                $incoming=1;
		print "\nINC line $in_message - $line\n";
		}
                if ($incoming ==1 && $line =~ /^REGISTER/ ){
		print "INC line $in_message - $line\n";
                }
		if ($incoming ==1 && $line =~ /^From/){
                print "INC line $in_message - $line\n";
                }
		if ($incoming ==1 && $line =~ /^CSeq/){
                print "INC line $in_message - $line\n";
                }
###
### OUTGOING messages processing
###
		if ($line =~ /proxy\[.*\]: SENDING message to/ ){
		$outgoing=1;
                print "\nOUT line $in_message - $line\n"
		}
                if ($outgoing==1 && $line =~ /^SIP\/2.0/){
		print "OUT line $in_message - $line\n"
		}
		if ($outgoing ==1 && $line =~ /^From/){
                print "OUT line $in_message - $line\n";
                }
                if ($outgoing ==1 && $line =~ /^CSeq/){
                print "OUT line $in_message - $line\n";
                }	
        }		   
     }
###
### FOR EMPTY LINES
###
     else{
     $in_message=0;
     $incoming=0;
     $outgoing=0;
#     print "$line\n";
     }
}
print "\nTOTAL Lines Processed: $lines_count\n";



close(HANDLE);

####    
#sub trim
#{
#    my $string = shift;

#    $string =~ s/^\s+//;
#    $string =~ s/\s+$//;

#    return $string;
#}

