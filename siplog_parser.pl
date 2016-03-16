#!/usr/bin/perl

use strict;
use warnings;

my $file1="sip_log";
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

<<'Request Example';
####################################


16 Mar 10:55:12.049/GLOBAL/proxy[12583]: RECEIVED message from 7.20.5.30:5060:
REGISTER sip:sip.o-lolo.co SIP/2.0
Via: SIP/2.0/UDP 192.168.0.10:5060;rport;branch=z9hG4bKeae2f0b097
From: "1111111111" <sip:1111111111@sip.o-lolo.co>;tag=0581d3c5
To: "1111111111" <sip:1111111111@sip.o-lolo.co>
Call-ID: 3330de9d4d672fac316aece762e74b09@192.168.0.10
Contact: <sip:1111111111@192.168.0.10:5060>
CSeq: 24911 REGISTER
Max-Forwards: 70
Expires: 60
Allow: INVITE,CANCEL,ACK,BYE,NOTIFY,REFER,OPTIONS,INFO,MESSAGE,UPDATE
Authorization: Digest username="1111111111",realm="sip.o-lolo.co",nonce="1458125601:2396a98f760855aa9b6dd8fed5ccdc64",response="0e38ae3894a6ddfe95e703f43f58189b",uri="sip:o-lolo.co",algorithm=MD5
User-Agent: CM5K-TA2S  (904290)
Content-Length: 0


16 Mar 10:55:12.066/GLOBAL/proxy[12583]: SENDING message to 7.20.5.30:5060:
SIP/2.0 200 Auth failed
Via: SIP/2.0/UDP 192.168.0.10:5060;rport=5060;branch=z9hG4bKeae2f0b097;received=7.20.5.30
Contact: <sip:1.1.1.1:5060>
To: "1111111111"<sip:48327976616@sip.o-lolo.co>;tag=b2c39c68
From: "1111111111"<sip:48327976616@sip.o-lolo.co>;tag=0581d3c5
Call-ID: 3330de9d4d672fac316aece762e74b09@192.168.0.10
CSeq: 24911 REGISTER
Content-Length: 0






####################################
Request Example


####    
sub trim
{
#    my $string = shift;

#    $string =~ s/^\s+//;
#    $string =~ s/\s+$//;

#    return $string;
#}

