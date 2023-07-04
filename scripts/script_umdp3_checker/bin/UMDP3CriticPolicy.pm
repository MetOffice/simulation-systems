# *****************************COPYRIGHT*******************************
# (C) Crown copyright Met Office. All rights reserved.
# For further details please refer to the file COPYRIGHT.txt
# which you should have received as part of this distribution.
# *****************************COPYRIGHT*******************************

package UMDP3CriticPolicy;
use strict;
use warnings;
use 5.010;

use Perl::Critic;

# Declare version - this is the last UM version this script was updated for:
our $VERSION = '13.2.0';

my @allowed_spellings = qw(CreateBC FCM UMUI NEMO CICE);

sub get_umdp3_critic_policy {

    # define overriden policies
    my %overriden_policies = ();
    $overriden_policies{'Documentation::PodSpelling'} =
      { 'stop_words' => join q{ }, @allowed_spellings };

    # Construct the critic policy with overriden policies omitted
    my @default_policies =
      Perl::Critic->new( -severity => 1, -exclude => keys %overriden_policies )
      ->policies();
    my $policy_file = Perl::Critic->new( -include => \@default_policies );

    # add back in the overridden policies with new settings
    for ( keys %overriden_policies ) {
        $policy_file->add_policy(
            -policy => $_,
            -params => $overriden_policies{$_}
        );
    }

    return $policy_file;
}

1;
