import gettext
_ = gettext.gettext

SDP_SERVER_SVCLASS_ID		= 0x1000
BROWSE_GRP_DESC_SVCLASS_ID	= 0x1001
PUBLIC_BROWSE_GROUP		= 0x1002
SERIAL_PORT_SVCLASS_ID		= 0x1101
LAN_ACCESS_SVCLASS_ID		= 0x1102
DIALUP_NET_SVCLASS_ID		= 0x1103
IRMC_SYNC_SVCLASS_ID		= 0x1104
OBEX_OBJPUSH_SVCLASS_ID		= 0x1105
OBEX_FILETRANS_SVCLASS_ID	= 0x1106
IRMC_SYNC_CMD_SVCLASS_ID	= 0x1107
HEADSET_SVCLASS_ID		= 0x1108
CORDLESS_TELEPHONY_SVCLASS_ID	= 0x1109
AUDIO_SOURCE_SVCLASS_ID		= 0x110a
AUDIO_SINK_SVCLASS_ID		= 0x110b
AV_REMOTE_TARGET_SVCLASS_ID	= 0x110c
ADVANCED_AUDIO_SVCLASS_ID	= 0x110d
AV_REMOTE_SVCLASS_ID		= 0x110e
VIDEO_CONF_SVCLASS_ID		= 0x110f
INTERCOM_SVCLASS_ID		= 0x1110
FAX_SVCLASS_ID			= 0x1111
HEADSET_AGW_SVCLASS_ID		= 0x1112
WAP_SVCLASS_ID			= 0x1113
WAP_CLIENT_SVCLASS_ID		= 0x1114
PANU_SVCLASS_ID			= 0x1115
NAP_SVCLASS_ID			= 0x1116
GN_SVCLASS_ID			= 0x1117
DIRECT_PRINTING_SVCLASS_ID	= 0x1118
REFERENCE_PRINTING_SVCLASS_ID	= 0x1119
IMAGING_SVCLASS_ID		= 0x111a
IMAGING_RESPONDER_SVCLASS_ID	= 0x111b
IMAGING_ARCHIVE_SVCLASS_ID	= 0x111c
IMAGING_REFOBJS_SVCLASS_ID	= 0x111d
HANDSFREE_SVCLASS_ID		= 0x111e
HANDSFREE_AGW_SVCLASS_ID	= 0x111f
DIRECT_PRT_REFOBJS_SVCLASS_ID	= 0x1120
REFLECTED_UI_SVCLASS_ID		= 0x1121
BASIC_PRINTING_SVCLASS_ID	= 0x1122
PRINTING_STATUS_SVCLASS_ID	= 0x1123
HID_SVCLASS_ID			= 0x1124
HCR_SVCLASS_ID			= 0x1125
HCR_PRINT_SVCLASS_ID		= 0x1126
HCR_SCAN_SVCLASS_ID		= 0x1127
CIP_SVCLASS_ID			= 0x1128
VIDEO_CONF_GW_SVCLASS_ID	= 0x1129
UDI_MT_SVCLASS_ID		= 0x112a
UDI_TA_SVCLASS_ID		= 0x112b
AV_SVCLASS_ID			= 0x112c
SAP_SVCLASS_ID			= 0x112d
PBAP_PCE_SVCLASS_ID		= 0x112e
PBAP_PSE_SVCLASS_ID		= 0x112f
PBAP_SVCLASS_ID			= 0x1130
PNP_INFO_SVCLASS_ID		= 0x1200
GENERIC_NETWORKING_SVCLASS_ID	= 0x1201
GENERIC_FILETRANS_SVCLASS_ID	= 0x1202
GENERIC_AUDIO_SVCLASS_ID	= 0x1203
GENERIC_TELEPHONY_SVCLASS_ID	= 0x1204
UPNP_SVCLASS_ID			= 0x1205
UPNP_IP_SVCLASS_ID		= 0x1206
UPNP_PAN_SVCLASS_ID		= 0x1300
UPNP_LAP_SVCLASS_ID		= 0x1301
UPNP_L2CAP_SVCLASS_ID		= 0x1302
VIDEO_SOURCE_SVCLASS_ID		= 0x1303
VIDEO_SINK_SVCLASS_ID		= 0x1304
VIDEO_DISTRIBUTION_SVCLASS_ID	= 0x1305
MDP_SVCLASS_ID			= 0x1400
MDP_SOURCE_SVCLASS_ID		= 0x1401
MDP_SINK_SVCLASS_ID		= 0x1402
APPLE_AGENT_SVCLASS_ID		= 0x2112

uuid_names = {}
uuid_names[0x0001] = "SDP"
uuid_names[0x0002] = "UDP"
uuid_names[0x0003] = "RFCOMM"
uuid_names[0x0004] = "TCP"
uuid_names[0x0005] = "TCS-BIN"
uuid_names[0x0006] = "TCS-AT"
uuid_names[0x0008] = "OBEX"
uuid_names[0x0009] = "IP"
uuid_names[0x000a] = "FTP"
uuid_names[0x000c] = "HTTP"
uuid_names[0x000e] = "WSP"
uuid_names[0x000f] = "BNEP"
uuid_names[0x0010] = "UPnP/ESDP"
uuid_names[0x0011] = "HIDP"
uuid_names[0x0012] = "Hardcopy Control Channel"
uuid_names[0x0014] = "Hardcopy Data Channel"
uuid_names[0x0016] = "Hardcopy Notification"
uuid_names[0x0017] = "AVCTP"
uuid_names[0x0019] = "AVDTP"
uuid_names[0x001b] = "CMTP"
uuid_names[0x001d] = "UDI_C-Plane"
uuid_names[0x0100] = "L2CAP"
uuid_names[0x1000] = "ServiceDiscoveryServerServiceClassID",
uuid_names[0x1001] = "BrowseGroupDescriptorServiceClassID"
uuid_names[0x1002] = "Public Browse Group"
uuid_names[0x1101] = "Serial Port"
uuid_names[0x1102] = "LAN Access Using PPP"
uuid_names[0x1103] = _("Dialup Networking (DUN)")
uuid_names[0x1104] = "IrMC Sync"
uuid_names[0x1105] = "OBEX Object Push"
uuid_names[0x1106] = "OBEX File Transfer"
uuid_names[0x1107] = "IrMC Sync Command"
uuid_names[0x1108] = "Headset"
uuid_names[0x1109] = "Cordless Telephony"
uuid_names[0x110a] = _("Audio Source")
uuid_names[0x110b] = _("Audio Sink")
uuid_names[0x110c] = "Remote Control Target"
uuid_names[0x110d] = "Advanced Audio"
uuid_names[0x110e] = "Remote Control"
uuid_names[0x110f] = "Video Conferencing"
uuid_names[0x1110] = "Intercom"
uuid_names[0x1111] = "Fax"
uuid_names[0x1112] = "Headset Audio Gateway"
uuid_names[0x1113] = "WAP"
uuid_names[0x1114] = "WAP Client"
uuid_names[0x1115] = "PANU"
uuid_names[0x1116] = _("Network Access Point")
uuid_names[0x1117] = _("Group Network")
uuid_names[0x1118] = "DirectPrinting (BPP)"
uuid_names[0x1119] = "ReferencePrinting (BPP)"
uuid_names[0x111a] = "Imaging (BIP)"
uuid_names[0x111b] = "ImagingResponder (BIP)"
uuid_names[0x111c] = "ImagingAutomaticArchive (BIP)"
uuid_names[0x111d] = "ImagingReferencedObjects (BIP)"
uuid_names[0x111e] = "Handsfree"
uuid_names[0x111f] = "Handsfree Audio Gateway"
uuid_names[0x1120] = "DirectPrintingReferenceObjectsService (BPP)"
uuid_names[0x1121] = "ReflectedUI (BPP)"
uuid_names[0x1122] = "Basic Printing (BPP)"
uuid_names[0x1123] = "Printing Status (BPP)"
uuid_names[0x1124] = "Human Interface Device Service (HID)"
uuid_names[0x1125] = "HardcopyCableReplacement (HCR)"
uuid_names[0x1126] = "HCR_Print (HCR)"
uuid_names[0x1127] = "HCR_Scan (HCR)"
uuid_names[0x1128] = "Common ISDN Access (CIP)"
uuid_names[0x1129] = "VideoConferencingGW (VCP)"
uuid_names[0x112a] = "UDI-MT"
uuid_names[0x112b] = "UDI-TA"
uuid_names[0x112c] = "Audio/Video"
uuid_names[0x112d] = "SIM Access (SAP)"
uuid_names[0x112e] = "Phonebook Access (PBAP) - PCE"
uuid_names[0x112f] = "Phonebook Access (PBAP) - PSE"
uuid_names[0x1130] = "Phonebook Access (PBAP)"
uuid_names[0x1200] = "PnP Information"
uuid_names[0x1201] = "Generic Networking"
uuid_names[0x1202] = "Generic FileTransfer"
uuid_names[0x1203] = "Generic Audio"
uuid_names[0x1204] = "Generi cTelephony"
uuid_names[0x1303] = "Video Source"
uuid_names[0x1304] = "Video Sink"
uuid_names[0x1305] = "Video Distribution"
uuid_names[0x1400] = "MDP"
uuid_names[0x1401] = "MDPSource"
uuid_names[0x1402] = "MDPSink"
uuid_names[0x2112] = "AppleAgent"


def uuid16_to_name(uuid16):
	try:
		return uuid_names[uuid16]
	except:
		return "Unknown"

def uuid128_to_uuid16(uuid128):
	try:
		return int('0x'+uuid128[4:8], 16)
	except:
		return 0
		
def bluez_to_friendly_name(svc):
	if svc == "audiosink":
		return uuid_names[0x110b]
	elif svc == "audiosource":
		return uuid_names[0x110a]
	else:
		raise Exception

