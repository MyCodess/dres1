__________ bins-templates/vorlagen bash/shel for common usages __________
exit 3
-!! see for collected/fullScript ones /up1/w/docs_m/devres/bins_coll_devres
##------------ USAGE + HELP (/etc/services) : -----------------------
usage ()
{
    echo "Usage: ${0##*/} [--help | --status-all | <service> [<args>| --full-restart]]" 1>&2
    exit 1
}
help ()
{
    echo "Usage: ${0##*/} [<options> | <service> [<args> | --full-restart]]"
    echo "Available <options>:"
    echo "  -h,--help        This help."
    echo "  -s,--status-all  List out status of all services."
    echo "Usage for specific <service>:"
    echo "  ${0##*/} service_name argument [option]"
    echo "  ${0##*/} service_name --full-restart"
    echo "  ${0##*/} --full-restart service_name"
    exit 0
}
##--------------------------------------------------------------------
