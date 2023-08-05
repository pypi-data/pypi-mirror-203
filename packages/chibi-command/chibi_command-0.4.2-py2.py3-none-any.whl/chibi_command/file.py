from chibi_hybrid.chibi_hybrid import Chibi_hybrid
from chibi_command import Command


class Tar( Command ):
    """
    Examples
    ========
    >>>command = Tar.verbose().extract().file( 'file.tar' )
    >>>command = command.output_directory( '/tmp/' )
    >>>command.preview()
    tar -v -x -f file.tar -C /tmp/
    >>>command.run()
    """
    command = 'tar'

    @Chibi_hybrid
    def extract( cls ):
        return cls( '-x' )

    @extract.instancemethod
    def extract( self ):
        self.add_args( '-x' )
        return self

    @Chibi_hybrid
    def file( cls, tar_file ):
        return cls( '-f', tar_file )

    @file.instancemethod
    def file( self, tar_file ):
        self.add_args( '-f', tar_file )
        return self

    @Chibi_hybrid
    def verbose( cls ):
        return cls( '-v' )

    @verbose.instancemethod
    def verbose( self ):
        self.add_args( '-v' )
        return self

    @Chibi_hybrid
    def output_directory( cls, path ):
        return cls( '-C', path )

    @output_directory.instancemethod
    def output_directory( self, path ):
        self.add_args( '-C', path )
        return self


class Bsdtar( Command ):
    command = 'bsdtar'
