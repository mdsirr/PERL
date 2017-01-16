
			use Data::Dumper qw( Dumper );

			my $cgi = CGI->new();
			my %form;
			for my $param ($cgi->param()) {
			   $form{$param} = [ $cgi->param($param) ];
			}
			
			print($cgi->header('text/plain'));
			
			local $Data::Dumper::Indent   = 1;
			local $Data::Dumper::Sortkeys = 1;
			local $Data::Dumper::Useqq    = 1;
			print(Dumper(\%form));
