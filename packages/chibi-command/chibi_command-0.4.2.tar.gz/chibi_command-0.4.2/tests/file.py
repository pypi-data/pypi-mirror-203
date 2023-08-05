from unittest import TestCase

from chibi_command.file import Tar


class Test_tar( TestCase ):
    def test_should_return_the_preview_expected( self ):
        expected = 'tar -v -x -f file.tar -C /tmp/'
        command = Tar.verbose().extract().file( 'file.tar' )
        command = command.output_directory( '/tmp/' )
        self.assertEqual( command.preview(), expected )
