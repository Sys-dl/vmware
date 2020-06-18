import wx
import os
import glob
import shutil
import codecs
import gzip
import linecache
import sys
import datetime

#display a popup about vm-support directory path
#user must set parent folder of vm-support
app = wx.App()
dialog = wx.DirDialog(None, u'Choose VM-support Folder', style=wx.DD_CHANGE_DIR)
dialog.ShowModal()
while not os.path.exists("./commands/" and "./var/run/log/"):
    dialog = wx.DirDialog(None, u'Choose VM-support Folder', style=wx.DD_CHANGE_DIR)
    dialog.ShowModal()





# checking file existence
#if you find that the tool say "missing xxx.txt", itselves is not warning error(just a report)

IMPORTANT_FILE = ["./commands/date.txt",\
                  "./commands/bootOption_-oC.txt",\
                  "./commands/cat_varlogvvoldlog.txt",\
                  "./commands/clom-tool_fitness-config-get.txt",\
                  "./commands/cmmds-tool_find--f-python.txt",\
                  "./commands/cmmds-tool_-f-json-readdump--p--d-scratchlogcmmdsdump.txt",\
                  "./commands/df.txt",\
                  "./commands/diagRP_--path-to-gid.txt",\
                  "./commands/dump-cswitch-info.py.txt",\
                  "./commands/esxcfg-module_-q.txt",\
                  "./commands/esxcfg-mpath_-b.txt",\
                  "./commands/esxcfg-route_-f-V6--l.txt",\
                  "./commands/esxcfg-route_-l.txt",\
                  "./commands/fcdInfo.py.tgz",\
                  "./commands/fdisk_-lu.txt",\
                  "./commands/fdm-dump.sh.txt",\
                  "./commands/hostd.sh.txt",\
                  "./commands/indcfg_--list---debug.txt",\
                  "./commands/irqinfo.txt",\
                  "./commands/lldpnetmap.txt",\
                  "./commands/localcli_fcoe-adapter-list.txt",\
                  "./commands/localcli_fcoe-nic-list.txt",\
                  "./commands/localcli_graphics-device-stats-list.txt",\
                  "./commands/localcli_hardware-ipmi-bmc-get.txt",\
                  "./commands/localcli_hardware-ipmi-fru-get--p--i--n-all.txt",\
                  "./commands/localcli_hardware-ipmi-fru-list--p--i--n-all.txt",\
                  "./commands/localcli_hardware-ipmi-sdr-get--p--i--n-all.txt",\
                  "./commands/localcli_hardware-ipmi-sdr-list--p--i--n-all.txt",\
                  "./commands/localcli_hardware-ipmi-sel-get--p--i--n-all.txt",\
                  "./commands/localcli_hardware-ipmi-sel-list--p--i--n-all.txt",\
                  "./commands/localcli_hardware-pci-list.txt",\
                  "./commands/localcli_hardware-trustedboot-get.txt",\
                  "./commands/localcli_iscsi-logicalnetworkportal-list.txt",\
                  "./commands/localcli_iscsi-physicalnetworkportal-list.txt",\
                  "./commands/localcli_iscsi-software-get.txt",\
                  "./commands/localcli_network-ip-connection-list.txt",\
                  "./commands/localcli_network-ip-neighbor-list.txt",\
                  "./commands/localcli_network-multicast-group-list.txt",\
                  "./commands/localcli_network-vswitch-dvs-vmware-lacp-config-get.txt",\
                  "./commands/localcli_network-vswitch-dvs-vmware-lacp-stats-get.txt",\
                  "./commands/localcli_network-vswitch-dvs-vmware-lacp-status-get.txt",\
                  "./commands/localcli_--plugin-dir-usrlibvmwareesxcliint-device-driver-list.txt",\
                  "./commands/localcli_--plugin-dir-usrlibvmwareesxcliint-storage-internal-vvol-daemon-set---dump-objects.txt",\
                  "./commands/localcli_--plugin-dir-usrlibvmwareesxcliint-systemInternal-coredump-configuration-check.txt",\
                  "./commands/localcli_software-acceptance-get.txt",\
                  "./commands/localcli_software-profile-get.txt",\
                  "./commands/localcli_software-profile-get---rebooting-image.txt",\
                  "./commands/localcli_software-vib-get.txt",\
                  "./commands/localcli_software-vib-get---rebooting-image.txt",\
                  "./commands/localcli_software-vib-list.txt",\
                  "./commands/localcli_storage-core-adapter-list.txt",\
                  "./commands/localcli_storage-core-adapter-stats-get.txt",\
                  "./commands/localcli_storage-core-claimrule-list---claimrule-classall.txt",\
                  "./commands/localcli_storage-core-device-capacity-list.txt",\
                  "./commands/localcli_storage-core-device-detached-list.txt",\
                  "./commands/localcli_storage-core-device-list.txt",\
                  "./commands/localcli_storage-core-device-list---pe-only.txt",\
                  "./commands/localcli_storage-core-device-partition-list.txt",\
                  "./commands/localcli_storage-core-device-partition-showguid.txt",\
                  "./commands/localcli_storage-core-device-stats-get.txt",\
                  "./commands/localcli_storage-core-device-vaai-ats-list.txt",\
                  "./commands/localcli_storage-core-device-vaai-clone-list.txt",\
                  "./commands/localcli_storage-core-device-vaai-delete-list.txt",\
                  "./commands/localcli_storage-core-device-vaai-status-get.txt",\
                  "./commands/localcli_storage-core-device-vaai-zero-list.txt",\
                  "./commands/localcli_storage-core-path-list.txt",\
                  "./commands/localcli_storage-core-plugin-registration-list.txt",\
                  "./commands/localcli_storage-filesystem-list--i.txt",\
                  "./commands/localcli_storage-iofilter-list.txt",\
                  "./commands/localcli_storage-nfs41-list.txt",\
                  "./commands/localcli_storage-nfs-list.txt",\
                  "./commands/localcli_storage-nfs-list---pe-only.txt",\
                  "./commands/localcli_storage-nmp-device-list.txt",\
                  "./commands/localcli_storage-nmp-path-list.txt",\
                  "./commands/localcli_storage-nmp-satp-rule-list.txt",\
                  "./commands/localcli_storage-san-fc-events-get.txt",\
                  "./commands/localcli_storage-san-fc-list.txt",\
                  "./commands/localcli_storage-san-fcoe-list.txt",\
                  "./commands/localcli_storage-san-fcoe-stats-get.txt",\
                  "./commands/localcli_storage-san-fc-stats-get.txt",\
                  "./commands/localcli_storage-san-iscsi-list.txt",\
                  "./commands/localcli_storage-san-iscsi-stats-get.txt",\
                  "./commands/localcli_storage-san-sas-list.txt",\
                  "./commands/localcli_storage-san-sas-stats-get.txt",\
                  "./commands/localcli_storage-vmfs-extent-list.txt",\
                  "./commands/localcli_storage-vmfs-lockmode-list--i.txt",\
                  "./commands/localcli_storage-vmfs-snapshot-list.txt",\
                  "./commands/localcli_storage-vvol-protocolendpoint-list.txt",\
                  "./commands/localcli_storage-vvol-storagecontainer-list.txt",\
                  "./commands/localcli_storage-vvol-vasaprovider-list.txt",\
                  "./commands/localcli_system-coredump-file-get.txt",\
                  "./commands/localcli_system-coredump-file-list.txt",\
                  "./commands/localcli_system-coredump-partition-get.txt",\
                  "./commands/localcli_system-coredump-partition-list.txt",\
                  "./commands/localcli_system-settings-advanced-list--d.txt",\
                  "./commands/localcli_system-settings-kernel-list--d.txt",\
                  "./commands/localcli_system-slp-search.txt",\
                  "./commands/localcli_system-slp-stats-get.txt",\
                  "./commands/localcli_system-stats-uptime-get.txt",\
                  "./commands/localcli_system-visorfs-get.txt",\
                  "./commands/localcli_system-visorfs-ramdisk-list.txt",\
                  "./commands/localcli_system-visorfs-tardisk-list.txt",\
                  "./commands/localcli_system-wbem-get.txt",\
                  "./commands/localcli_system-wbem-provider-list.txt",\
                  "./commands/localcli_vm-process-list.txt",\
                  "./commands/localcli_vsan-cluster-get.txt",\
                  "./commands/localcli_vsan-cluster-unicastagent-list.txt",\
                  "./commands/localcli_vsan-debug-controller-list.txt",\
                  "./commands/localcli_vsan-debug-disk-list.txt",\
                  "./commands/localcli_vsan-debug-limit-get.txt",\
                  "./commands/localcli_vsan-debug-memory-list.txt",\
                  "./commands/localcli_vsan-debug-object-health-summary-get.txt",\
                  "./commands/localcli_vsan-debug-object-list.txt",\
                  "./commands/localcli_vsan-debug-object-overview.txt",\
                  "./commands/localcli_vsan-debug-resync-list.txt",\
                  "./commands/localcli_vsan-debug-resync-summary-get.txt",\
                  "./commands/localcli_vsan-network-list.txt",\
                  "./commands/localcli_vsan-perf-status-get.txt",\
                  "./commands/localcli_vsan-storage-list.txt",\
                  "./commands/ls_-isla-.txt",\
                  "./commands/ls_-islR-dev.txt",\
                  "./commands/ls_-isl-vmfsvolumes.txt",\
                  "./commands/lspci.txt",\
                  "./commands/lspci_-v.txt",\
                  "./commands/lsusb.txt",\
                  "./commands/lsusb_-t.txt",\
                  "./commands/lsusb_-v.txt",\
                  "./commands/lw-lsa_get-metrics.txt",\
                  "./commands/lw-lsa_get-status.txt",\
                  "./commands/lw-lsa_trace-info.txt",\
                  "./commands/memstats_-r-uw-stats.txt",\
                  "./commands/net-dvs_-l.txt",\
                  "./commands/net-stats_-l.txt",\
                  "./commands/nicinfo.sh.txt",\
                  "./commands/ntpq_-c-kerninfo.txt",\
                  "./commands/ntpq_-c-readvar.txt",\
                  "./commands/ntpq_-c-version.txt",\
                  "./commands/ntpq_-p.txt",\
                  "./commands/partedUtil.sh.txt",\
                  "./commands/prettyPrint.sh_clusterconfig.txt",\
                  "./commands/prettyPrint.sh_hostlist.txt",\
                  "./commands/prettyPrint.sh_vmmetadata.txt",\
                  "./commands/ps_-Cc---tree.txt",\
                  "./commands/ps_-cPTgjstz.txt",\
                  "./commands/python_usrlibvmwarevsanperfsvcVsanLsomHealthpyc.txt",\
                  "./commands/python_usrlibvmwarevsanperfsvcvsan-perfsvc-statuspyc-perf_stats_with_dump.txt",\
                  "./commands/python_usrlibvmwarevsanperfsvcvsan-perfsvc-statuspyc-svc_info.txt",\
                  "./commands/python_usrlibvmwarevsanperfsvcvsan-perfsvc-statuspyc---unit-hour-perf_stats_with_dump_diag-1.txt",\
                  "./commands/rdmainfo.sh.txt",\
                  "./commands/secpolicytools_-d.txt",\
                  "./commands/sensord_-v--l--D.txt",\
                  "./commands/sh_-c-binmd5sum(findbin-typef).txt",\
                  "./commands/sh_-c-binmd5sum(findlib64-typef).txt",\
                  "./commands/sh_-c-binmd5sum(findlib-typef).txt",\
                  "./commands/sh_-c-binmd5sum(findsbin-typef).txt",\
                  "./commands/smartinfo.txt",\
                  "./commands/smbios.bin",\
                  "./commands/smbiosDump.txt",\
                  "./commands/storageHostProfiles.sh.txt",\
                  "./commands/summarize-dvfilter.txt",\
                  "./commands/swfw.sh.txt",\
                  "./commands/esxcfg-vmknic_-l.txt",\
                  "./commands/esxcfg-vswitch_-l.txt",\
                  "./commands/tracenet.txt",\
                  "./commands/uname_-a.txt",\
                  "./commands/uwstats_-s-all.txt",\
                  "./commands/vdq_-q--H.txt",\
                  "./commands/vdu_-a-.txt",\
                  "./commands/vFlash.sh.txt",\
                  "./commands/vmkerrcode_-l.txt",\
                  "./commands/vmkiscsid_--dump-db.txt",\
                  "./commands/vmkload_mod_-v10--l.txt",\
                  "./commands/vmkmgmt_keyval_-a.txt",\
                  "./commands/vmkping_-D--v.txt",\
                  "./commands/vmkvsitools_lsof.txt",\
                  "./commands/vmware_-vl.txt",\
                  "./commands/vobbuf_-h.txt",\
                  "./commands/vsantraced_flush.txt",\
                  "./commands/vsish_-e-get-vmkModulestracingstats.txt",\
                  "./var/run/log/auth.log",\
                  "./var/run/log/clomd.log",\
                  "./var/run/log/clusterAgent.log",\
                  "./var/run/log/cmmdsTimeMachine.log",\
                  "./var/run/log/cmmdsTimeMachineDump.log",\
                  "./var/run/log/ddecomd.log",\
                  "./var/run/log/dhclient.log",\
                  "./var/run/log/epd.log",\
                  "./var/run/log/esxupdate.log",\
                  "./var/run/log/fdm.log",\
                  "./var/run/log/hbragent.log",\
                  "./var/run/log/hbrca.log",\
                  "./var/run/log/hostd.log",\
                  "./var/run/log/hostdCgiServer.log",\
                  "./var/run/log/hostd-probe.log",\
                  "./var/run/log/hostprofiletrace.log",\
                  "./var/run/log/iofiltervpd.log",\
                  "./var/run/log/lacp.log",\
                  "./var/run/log/loadESX.log",\
                  "./var/run/log/nfcd.log",\
                  "./var/run/log/osfsd.log",\
                  "./var/run/log/rabbitmqproxy.log",\
                  "./var/run/log/rhttpproxy.log",\
                  "./var/run/log/sdrsinjector.log",\
                  "./var/run/log/shell.log",\
                  "./var/run/log/storagerm.log",\
                  "./var/run/log/swapobjd.log",\
                  "./var/run/log/syslog.log",\
                  "./var/run/log/upitd.log",\
                  "./var/run/log/usb.log",\
                  "./var/run/log/vit.conf.backup",\
                  "./var/run/log/vitd.log",\
                  "./var/run/log/vmauthd.log",\
                  "./var/run/log/vmkdevmgr.log",\
                  "./var/run/log/vmkeventd.log",\
                  "./var/run/log/vmksummary.log",\
                  "./var/run/log/vmkwarning.log",\
                  "./var/run/log/vmsyslogd-dropped.log",\
                  "./var/run/log/vobd.log",\
                  "./var/run/log/vprobe.log",\
                  "./var/run/log/vpxa.log",\
                  "./var/run/log/vsandpd.log",\
                  "./var/run/log/vsanmgmt.log",\
                  "./var/run/log/vsansystem.log",\
                  "./var/run/log/vsanvpd.log",\
                  "./var/run/log/vsanvpd.log",\
                  "./var/run/log/vvold.log",\
                  "./var/run/log/Xorg.log",\
                  ]

CURRENTPATH = os.getcwd()


sys.stdout = open("./Elenore.txt", "w")
print("file existing check...\n \n")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n \n file existing check...\n \n")
for IMP in IMPORTANT_FILE:
    if os.path.exists(IMP):
        pass
    else:
        sys.stdout = open("./Elenore.txt", "a")
        print(IMP + "   is Missing")
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        print(IMP + "   is Missing")


##showing the directory that elenore tool recognized
sys.stdout = open("./Elenore.txt", "a")
print("\n \n ********** FOLDER ********** ")
print("FOLDER:   " + CURRENTPATH)
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n \n ********** FOLDER ********** ")
print("FOLDER:   " + CURRENTPATH)











#display ESXi version
sys.stdout = open("./Elenore.txt", "a")
print("\n ********** VERSION ********** ")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n ********** VERSION ********** ")

if os.path.exists("./commands/vmware_-vl.txt"):
    FILE = "./commands/vmware_-vl.txt"
    OBJECT = open(versionfile)
    TEXT = OBJECT.read()
    OBJECT.close()
    sys.stdout = open("./Elenore.txt", "a")
    print("Version:    " + TEXT + "   (from /commands/vmware -vl.txt)")
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("Version:    " + TEXT + "   (from /commands/vmware -vl.txt)")
else:
    print("./commands/vmware_-vl.txt is Missing...")






sys.stdout = open("./Elenore.txt", "a")
print("\n **********  BOOTBANK  ********** ")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n **********  BOOTBANK  ********** ")


if os.path.exists("./commands/vmkfstools_-P--v-10-bootbank.txt"):
    path = './commands/vmkfstools_-P--v-10-bootbank.txt'
    with open(path) as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        Bootbank = [line for line in lines_strip if 'Logical device:' in line]
        sys.stdout = open("./Elenore.txt", "a")
        print(Bootbank[0] + "    (from /commands/vmkfstools_-P--v-10-bootbank.txt)")
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        print(Bootbank[0] + "    (from /commands/vmkfstools_-P--v-10-bootbank.txt)")
else:
    print("./commands/vmkfstools_-P--v-10-bootbank.txt is Missing...  ")











#capturing time
sys.stdout = open("./Elenore.txt", "a")
print("\n ********** DATE and NTP ********** ")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n ********** DATE and NTP ********** ")

if os.path.exists("./commands/date.txt"):
    FILE = "./commands/date.txt"
    OBJECT = open(FILE)
    TEXT = OBJECT.read()
    OBJECT.close()
    sys.stdout = open("./Elenore.txt", "a")
    print("CaptureTime (from ./commands/date.txt):    " + TEXT)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("CaptureTime (from ./commands/date.txt):    " + TEXT)
else:
    print("./commands/date.txt is Missing...")

#display ntp setting
if os.path.exists("./etc/ntp.conf"):
    FILE = "./etc/ntp.conf"
    OBJECT = open(FILE)
    TEXT = OBJECT.read()
    OBJECT.close()
    sys.stdout = open("./Elenore.txt", "a")
    print("NTP setting (from ./etc/ntp.conf):    \n"+ TEXT)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("NTP setting (from ./etc/ntp.conf):    \n"+ TEXT)
else:
    print("/etc/ntp.conf is Missing...")











#display uptime
sys.stdout = open("./Elenore.txt", "a")
print("\n **********  UPTIME  ********** ")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n **********  UPTIME  ********** ")



#convert ms > day, hour, minute...
if os.path.exists("./commands/localcli_system-stats-uptime-get.txt"):
    UPTIME = "./commands/localcli_system-stats-uptime-get.txt"
    OBJECT = open(UPTIME)
    MS = OBJECT.read()
    OBJECT.close()
    UPT = datetime.timedelta(microseconds=int(MS))
    sys.stdout = open("./Elenore.txt", "a")
    print( "uptime:   " + str(UPT) + "  (from /commands/localcli_system-stats-uptime-get.txt)")
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("uptime:   " + str(UPT) + "  (from /commands/localcli_system-stats-uptime-get.txt)")
else:
    print("/commands/localcli_system-stats-uptime-get.txt is Missing...")












##hardware vendor, BIOS version, and so on.
sys.stdout = open("./Elenore.txt", "a")
print("\n **********  Server hardware Infomation  ********** ")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n **********  Server hardware Infomation  ********** ")

if os.path.exists("./commands/smbiosDump.txt"):
    PATH = './commands/smbiosDump.txt'
    with open(PATH) as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        BIOSversion = [line for line in lines_strip if 'Version: ' in line]
        TAG = [line for line in lines_strip if 'Serial:' in line]
        SRVproduct = [line for line in lines_strip if 'Product:' in line]
        sys.stdout = open("./Elenore.txt", "a")
        print("BIOS " + BIOSversion[0] + "    (from /commands/smbiosDump.txt)")
        print(TAG[0] + "    (from /commands/smbiosDump.txt)")
        print(SRVproduct[0] + "    (from /commands/smbiosDump.txt)")
        print("MotherBoard" + SRVproduct[1] + "    (from /commands/smbiosDump.txt)")
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        print("BIOS " + BIOSversion[0] + "    (from /commands/smbiosDump.txt)")
        print(TAG[0] + "    (from /commands/smbiosDump.txt)")
        print(SRVproduct[0] + "    (from /commands/smbiosDump.txt)")
        print("MotherBoard" + SRVproduct[1] + "    (from /commands/smbiosDump.txt)")
else:
    print("./commands/smbiosDump.txt is Missing...")










##for Dell EMC server, dispkay iDRAC Service Module version
if os.path.exists("./commands/localcli_software-vib-get.txt"):
    path = './commands/localcli_software-vib-get.txt'
    with open(path) as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        iSM = [line for line in lines_strip if 'Dell EMC iDRAC Service Module' in line]
        if not len(iSM) == 0:
            sys.stdout = open("./Elenore.txt", "a")
            print("iSM" + iSM[0] + "    (from /commands/localcli_software-vib-get.txt)")
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            print("iSM" + iSM[0] + "    (from /commands/localcli_software-vib-get.txt)")
        else:
            print("iSM is not installed!")
else:
    print("./commands/localcli_software-vib-get.txt is Missing...")







##vmhba adapter
sys.stdout = open("./Elenore.txt", "a")
print("\n \n \n ********** VMHBA ********** ")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n \n \n ********** VMHBA ********** ")

if os.path.exists("./commands/localcli_storage-core-adapter-list.txt"):
    PATH = './commands/localcli_storage-core-adapter-list.txt'
    FILE = "./commands/localcli_storage-core-adapter-list.txt"
    OBJECT = open(FILE)
    TEXT = OBJECT.read()
    OBJECT.close()
    sys.stdout = open("./Elenore.txt", "a")
    print("Adapter List (from /commands/localcli_storage-core-adapter-list.txt):    " + TEXT)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("Adapter List (from /commands/localcli_storage-core-adapter-list.txt):    " + TEXT)
    # for Dell EMC Server and if it has NVMe boot device, display it
    if "PCIe" or "nvme" in TEXT:
        sys.stdout = open("./Elenore.txt", "a")
        print("BOSS card KB: https://www.dell.com/support/article/jp/ja/jpbsd1/how16859/ja#2")
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        print("BOSS card KB: https://www.dell.com/support/article/jp/ja/jpbsd1/how16859/ja#2")
    else:
        pass
else:
    print("./commands/localcli_storage-core-adapter-list.txt is Missing...")














##multipath
sys.stdout = open("./Elenore.txt", "a")
print("\n \n \n ********** Disk Path ********** ")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n \n \n ********** Disk Path ********** ")

if os.path.exists("./commands/esxcfg-mpath_-b.txt"):
    FILE = "./commands/esxcfg-mpath_-b.txt"
    OBJECT = open(FILE)
    TEXT = OBJECT.read()
    OBJECT.close()
    sys.stdout = open("./Elenore.txt", "a")
    print("Adapter List (from /commands/esxcfg-mpath_-b.txt):    \n" + TEXT)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("Adapter List (from /commands/esxcfg-mpath_-b.txt):    \n" + TEXT)
else:
    sys.stdout = open("./Elenore.txt", "a")
    print("/commands/esxcfg-mpath_-b.txt  is Missing")
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("/commands/esxcfg-mpath_-b.txt  is Missing")











#enabled vSAN or not
PATH = './commands/localcli_vsan-cluster-get.txt'
with open(PATH) as f:
    lines = f.readlines()
    lines_strip = [line.strip() for line in lines]
    sys.stdout = open("./Elenore.txt", "a")
    print("\n **********  vSAN  ********* ")
    print(lines_strip[0])
    print(lines_strip[1] + "     (/commands/localcli_vsan-cluster-get.txt)")
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("\n **********  vSAN  ********* ")
    print(lines_strip[0])
    print(lines_strip[1] + "     (/commands/localcli_vsan-cluster-get.txt)")
    if "true" in lines_strip[1]:
        sys.stdout = open("./Elenore.txt", "a")
        print("vSAN Log KB: https://www.dell.com/support/article/jp/ja/jpbsd1/how16761/ja")
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        print("vSAN Log KB: https://www.dell.com/support/article/jp/ja/jpbsd1/how16761/ja")
        vSANC = "./commands/localcli_vsan-cluster-get.txt"
        if os.path.exists(vSANC):
            OBJECT = open(vSANC)
            VC = OBJECT.read()
            OBJECT.close()
            sys.stdout = open("./Elenore.txt", "a")
            print("\nvSAN Cluster Info (from ./commands/localcli_vsan-cluster-get.txt):    \n" + VC)
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            print("\nvSAN Cluster Info (from ./commands/localcli_vsan-cluster-get.txt):    \n" + VC)
    else:
        pass










###nicinfo(without error-counter such as CRC error)
sys.stdout = open("./Elenore.txt", "a")
print("\n ********** NICINFO ********** ")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n ********** NICINFO ********** ")
if os.path.exists("./commands/nicinfo.sh.txt"):
    f = open('./commands/nicinfo.sh.txt', 'r')
    line = f.readline()[36:]
    while line:
        if not "NIC:" in line:
            sys.stdout = open("./Elenore.txt", "a")
            print(line.strip())
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            print(line.strip())
            line = f.readline()
        else:
            break
    f.close()
else:
    print("/commands/nicinfo.sh.txt is Missing...")
sys.stdout = open("./Elenore.txt", "a")
print("# for more info; check /commands/nicinfo.sh.txt...")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("#for more information; check /commands/nicinfo.sh.txt...")




#vmknic

sys.stdout = open("./Elenore.txt", "a")
print("\n ********** VMKNIC and SWITCHES ********** \n")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n ********** VMKNIC and SWITCHES ********** \n")
if os.path.exists("./commands/esxcfg-vmknic_-l.txt"):
    FILE = "./commands/esxcfg-vmknic_-l.txt"
    OBJECT = open(FILE)
    TEXT = OBJECT.read()
    OBJECT.close()
    sys.stdout = open("./Elenore.txt", "a")
    print("vmk and switches (from ./commands/esxcfg-vmknic_-l.txt and /commands/esxcfg-vswitch_-l.txt):" + "\n" + TEXT)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("vmk and switches (from ./commands/esxcfg-vmknic_-l.txt and /commands/esxcfg-vswitch_-l.txt):" + "\n" + TEXT)
else:
    sys.stdout = open("./Elenore.txt", "a")
    print("/commands/esxcfg-vmknic_-l.txt is missing...")
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("/commands/esxcfg-vmknic_-l.txt is missing...")




#vswitch

if os.path.exists("./commands/esxcfg-vswitch_-l.txt"):
    FILE = "./commands/esxcfg-vswitch_-l.txt"
    OBJECT = open(FILE)
    TEXT = OBJECT.read()
    OBJECT.close()
    sys.stdout = open("./Elenore.txt", "a")
    print(TEXT)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print(TEXT)
else:
    sys.stdout = open("./Elenore.txt", "a")
    print("/commands/esxcfg-vswitch_-l.txt is missing...")
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("/commands/esxcfg-vswitch_-l.txt is missing...")





#datastore

sys.stdout = open("./Elenore.txt", "a")
print("\n ********** DATASTORE ********** ")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n ********** DATASTORE ********** ")
if os.path.exists("./commands/localcli_storage-vmfs-extent-list.txt"):
    FILE = "./commands/localcli_storage-vmfs-extent-list.txt"
    OBJECT = open(FILE)
    TEXT = OBJECT.read()
    OBJECT.close()
    sys.stdout = open("./Elenore.txt", "a")
    print("datastore list (from ./commands/localcli_storage-vmfs-extent-list.txt):" + "\n" + TEXT)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("datastore list (from ./commands/localcli_storage-vmfs-extent-list.txt):" + "\n" + TEXT)
else:
    sys.stdout = open("./Elenore.txt", "a")
    print("/commands/localcli_storage-vmfs-extent-list.txt is missing...")
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("/commands/localcli_storage-vmfs-extent-list.txt is missing...")




#Virtual Machine
#Warning: I have already known that an error may occured about this section rarely.

sys.stdout = open("./Elenore.txt", "a")
print("\n ********** VIRTUAL MACHINE ********** ")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n ********** VIRTUAL MACHINE ********** ")

if os.path.exists('./commands/localcli_vm-process-list.txt'):
    VMAMOUNT = (sum([1 for _ in codecs.open('./commands/localcli_vm-process-list.txt', 'r', 'utf_8')])) - 1
    sys.stdout = open("./Elenore.txt", "a")
    print("Total Number of VMs :  " + str(VMAMOUNT // 8) + "\n \n")
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("Total Number of VMs :  " + str(VMAMOUNT // 8) + "\n \n")
else:
    sys.stdout = open("./Elenore.txt", "a")
    print("/commands/localcli_vm-process-list.txt is Missing...")
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("/commands/localcli_vm-process-list.txt is Missing...")


rootDir = './vmfs/volumes/'
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    sys.stdout = open("./Elenore.txt", "a")
    print('Found directory: %s' % dirName)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print('Found directory: %s' % dirName)
    for fname in fileList:
        if not ".vmx" in fname:
            pass
        elif ".vmxf" in fname:
            pass
        else:
            sys.stdout = open("./Elenore.txt", "a")
            print("VM Name :  " + os.path.splitext(fname)[0])
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            print("VM Name :  " + os.path.splitext(fname)[0])
            VMX = (dirName +'\\'+ fname)
            with codecs.open(VMX, "r", "utf_8") as vmx:
                vmxline = vmx.readlines()
                v = [line for line in vmxline if "guestOS" in line]
                sys.stdout = open("./Elenore.txt", "a")
                if not len(v) == 0:
                    print(v[0].rstrip("\n"))
                    sys.stdout.close()
                    sys.stdout = sys.__stdout__
                    print(v[0].rstrip("\n"))
                else:
                    pass

                v = [line for line in vmxline if "annotation" in line]
                sys.stdout = open("./Elenore.txt", "a")
                if not len(v) == 0:
                    print(v[0])
                    sys.stdout.close()
                    sys.stdout = sys.__stdout__
                    print(v[0])
                else:
                    print("\n")
                    sys.stdout.close()
                    sys.stdout = sys.__stdout__
                    print("\n")












##exit elenore tool
sys.stdout = open("./Elenore.txt", "a")
print("\n All processing is complete")
sys.stdout.close()
sys.stdout = sys.__stdout__
print("\n ######  All processing is complete  ######")

answer = input("Do you want to create a text file on current folder[y/n]? \n ** if not, type[n]:as default:[y]: ")
if not answer in ["n"]:
    pass
elif answer in [""]:
    pass
else:
    os.remove("./Elenore.txt")

LAST = input("Press any key to close this window...")

