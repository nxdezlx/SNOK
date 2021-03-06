# coding:utf-8
'''
Created on 2020-10-14

@author: Dizzy
'''
from CDeviceType import CDeviceType
from CDeviceType import CDeviceVersion
from CDevice import CDevice
from selenium.webdriver.common.keys import Keys #需要引入 keys 包
from selenium.webdriver.support.select import Select
from const import Const
from selenium.webdriver.common.action_chains import ActionChains
import time

const = Const();
const.NAME_ACCOUNT = "account";
const.NAME_PASSWORD = "password";
const.NAME_SUBMIT = "btnSubmit";
const.LINK_TEXT_CONNECT_TO_INTERNET = "连接到因特网";
const.EXTEND_URL_WAN_NEW = "wan_new.asp";
const.EXTEND_URL_VLAN_ADD = "vlan_intf_set.asp";
const.EXTEND_URL_VLAN_PORT_SET = "vlan_port_set.asp";

class CDevice_H3C_ER3200G2(CDevice):
    '''
    classdocs
    '''

    def __init__(self, enDeviceVersion):
        '''
        Constructor
        '''
        CDevice.__init__(self);
        CDevice.SetDeviceType(self, CDeviceType.H3C_ER3200G2);
        CDevice.SetDeviceVersion(self, enDeviceVersion);
        
        
    def LoginInputUsernamePassword(self):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            self.GetBrowser().find_element_by_name(const.NAME_ACCOUNT).send_keys(self.GetUsername());
            self.GetBrowser().find_element_by_name(const.NAME_PASSWORD).send_keys(self.GetPassword());
        
    def LoginSubmit(self):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            self.GetBrowser().find_element_by_name(const.NAME_SUBMIT).send_keys(Keys.ENTER); 
        
    def ConnectToInternet_StaticLine(self):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_WAN_NEW);
            Select(self.GetBrowser().find_element_by_name("wan1IPMode")).select_by_index(0);
            self.GetBrowser().find_element_by_name("WAN1_IP").clear();
            self.GetBrowser().find_element_by_name("WAN1_IP").send_keys(CDevice.GetStaticLineIP(self));
            elementNetMask = self.GetBrowser().find_element_by_name("WAN1_NM");
            elementNetMask.clear();
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys((CDevice.GetStaticLineMask(self))[1:]);
            self.GetBrowser().find_element_by_name("WAN1_GW").clear();
            self.GetBrowser().find_element_by_name("WAN1_GW").send_keys(CDevice.GetStaticLineGateway(self));
            self.GetBrowser().find_element_by_name("WAN1_DS1").clear();
            self.GetBrowser().find_element_by_name("WAN1_DS1").send_keys(CDevice.GetStaticLineDNS1(self));
            self.GetBrowser().find_element_by_name("WAN1_DS2").clear();
            self.GetBrowser().find_element_by_name("WAN1_DS2").send_keys(CDevice.GetStaticLineDNS2(self));
            self.GetBrowser().find_element_by_xpath("//input[@value='应用'][@type='button']").click();
            CDevice.CloseTab(self);
        
    def ConnectToInternet_PPPoE(self):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_WAN_NEW);
            Select(self.GetBrowser().find_element_by_name("wan1IPMode")).select_by_index(2);
            self.GetBrowser().find_element_by_name("WAN1_PUN").clear();
            self.GetBrowser().find_element_by_name("WAN1_PUN").send_keys(CDevice.GetPPPoEAccountName(self));
            self.GetBrowser().find_element_by_name("WAN1_PPW").clear();
            self.GetBrowser().find_element_by_name("WAN1_PPW").send_keys(CDevice.GetPPPoEPassword(self));
            self.GetBrowser().find_element_by_xpath("//input[@value='应用'][@type='button']").click();
            CDevice.CloseTab(self);
        
    def AddVlanInterface(self, szVlanId, szInterfaceIp, szMask):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_VLAN_ADD);
            self.GetBrowser().find_element_by_name("op_new").click();
            self.GetBrowser().find_element_by_name("vlan_id").clear();
            self.GetBrowser().find_element_by_name("vlan_id").send_keys(szVlanId);
            self.GetBrowser().find_element_by_name("IP").clear();
            self.GetBrowser().find_element_by_name("IP").send_keys(szInterfaceIp);
            self.GetBrowser().find_element_by_name("mask").clear();
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(szMask[1:]);
            self.GetBrowser().find_element_by_name("amend").click();
            time.sleep(3)
            CDevice.CloseTab(self);
            
    def AddVlanToTrunk(self, nIndex):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_VLAN_PORT_SET);
            frameConfigureVlanPort = self.GetBrowser().find_element_by_tag_name("iframe");
            self.GetBrowser().switch_to_frame(frameConfigureVlanPort);
            #portLanSWElement = self.GetBrowser().find_elements_by_link_text("LAN1");
            #ActionChains(self.GetBrowser()).double_click(portLanSWElement).perform();
            #self.GetBrowser().find_element_by_xpath("//IMG["+ str(nIndex) + "]").click();
            self.GetBrowser().find_element_by_xpath("//table[@id='disableclick']/tbody/tr[" + str(nIndex + 1) + "]/td[1]").click();
            
            