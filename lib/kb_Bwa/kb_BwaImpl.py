# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class kb_Bwa:
    '''
    Module Name:
    kb_Bwa

    Module Description:
    A KBase module: kb_Bwa
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/man4ish/kb_Bwa.git"
    GIT_COMMIT_HASH = "5cd4cb691be7b7579a7e3ccd7fabd5cb1ada833e"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_kb_Bwa(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_kb_Bwa
        report = KBaseReport(self.callback_url)
        report_info = report.create({'report': {'objects_created':[],
                                                'text_message': params['parameter_1']},
                                                'workspace_name': params['workspace_name']})
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
        #END run_kb_Bwa

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_kb_Bwa return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
