'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<kh:account xmlns:co="http://cobra.topicus.nl/v0.1" xmlns:kh="http://keyhub.topicus.nl/v0.1">
    <co:link id="42" rel="self" type="auth.Account"
             href="https://keyhub.topicusonderwijs.nl/keyhub/rest/v1/account/42"/>
    <co:permission full="auth.Account:READ:INSTANCE(42)" type="auth.Account" operations="READ"
                   instances="INSTANCE(42)"/>
    <co:additionalObjects/>
    <kh:validity>VALID</kh:validity>
    <kh:uuid>826be695-a5a7-46bb-80ce-2730525900ee</kh:uuid>
    <kh:username>rando.cardissian</kh:username>
    <kh:displayName>Rando Cardissian</kh:displayName>
    <kh:twoFactorStatus>TOTP</kh:twoFactorStatus>
    <kh:active>true</kh:active>
    <kh:validInDirectory>true</kh:validInDirectory>
    <kh:canRequestGroups>true</kh:canRequestGroups>
    <kh:tokenPasswordEnabled>false</kh:tokenPasswordEnabled>
    <kh:keyHubPasswordChangeRequired>false</kh:keyHubPasswordChangeRequired>
    <kh:directoryPasswordChangeRequired>false</kh:directoryPasswordChangeRequired>
    <kh:email>rando.cardissian@topicus.nl</kh:email>
    <kh:lastActive>2018-05-03T13:18:07.662Z</kh:lastActive>
    <kh:permissions>
        <kh:permission full="KeyHubSecurityKeys$Profile:CREATE,READ,UPDATE,DELETE:SINGLETON(KEY)"
                       type="KeyHubSecurityKeys$Profile" operations="DELETE UPDATE READ CREATE"
                       instances="SINGLETON(KEY)"/>
        <kh:permission full="auth.Account:READ:INSTANCE(42)" type="auth.Account" operations="READ"
                       instances="INSTANCE(42)"/>
    </kh:permissions>
    <kh:directoryType>LDAP</kh:directoryType>
    <kh:directoryName>Topicus AD</kh:directoryName>
    <kh:locale>nl-NL</kh:locale>
</kh:account>'''